import streamlit as st
import subprocess
import json

def get_stack_list():
    # Execute AWS CLI command to list stacks
    try:
        output = subprocess.check_output(["aws", "cloudformation", "list-stacks"], universal_newlines=True)
        stacks_data = json.loads(output)
        stacks = stacks_data.get("StackSummaries", [])
        stack_names = [stack["StackName"] for stack in stacks]
        
        # Display the list of running stacks
        if stack_names:
            st.write("Running Stacks:")
            for stack_name in stack_names:
                st.code(stack_name)
        else:
            st.write("No running stacks found.")
        # return stack_names
    except subprocess.CalledProcessError:
        st.write("Failed to retrieve running stacks.")

