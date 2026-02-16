import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("API key not found")
    
    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt", nargs="+", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    user_prompt = " ".join(args.user_prompt)
 

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    for _ in range(20):
        res = client.models.generate_content(model="gemini-2.5-flash", contents=messages , config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt, temperature=0))
        metadata = res.usage_metadata
        if not metadata:
            raise RuntimeError("Failed API Request")
        if res.candidates:
            for c in res.candidates:
                messages.append(c.content)

    # call the model, handle responses, etc.
    
       

        if args.verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {metadata.prompt_token_count}")
            print(f"Response tokens: {metadata.candidates_token_count}")


        if not res.function_calls:
            print(res.text)
            return
    
        function_responses = []
        for call in res.function_calls:
            function_call_result = call_function(call, args.verbose)
            if not function_call_result.parts:
                raise Exception("Empty Parts list")
            if not function_call_result.parts[0].function_response:
                raise Exception("Missing function response in part")
            if not function_call_result.parts[0].function_response.response:
                raise Exception("Missing response in function response part")
            function_responses.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        messages.append(types.Content(role="user", parts=function_responses))
        
    print("Limit exceeded tried more than 20 times")
    exit(1)

        

if __name__ == "__main__":
    main()
