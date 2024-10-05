class Prompts:

    def __init__(self) -> None:
        pass

    def vision_prompt():
        return """
        You are an expert in understanding Images. You will get Medical reports so you have to extract all text from image.
        """

    def text_json_prompt():
        return """
        You are an expert in text comprehension. Your task is straightforward: understand the provided text and return the output in the specified JSON format.

        Text: {text}

        Output: Please provide the output in the following JSON format:

        {{
        "patient_name": "<patient name>",
        "lab_no": "<lab number>",
        "lab_name": "<laboratory name>",
        "collection_date_time": "<sample collection date and time>",
        "reported_date_time": "<report date and time>",
        "test_name": "<test name>",
        "patient_age": "<patient age>",
        "patient_gender": "<patient gender>",
        "Report": {{
            "<investigation name>": {{
            "result": "<result value>",
            "reference_value": "<reference range>",
            "unit": "<unit of measurement>"
            }}
        }}
        }}
        """
