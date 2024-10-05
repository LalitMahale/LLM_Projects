class Prompts:

    def vision_prompt():
        return """
        You are an expert in understanding Images. You will get Medical reports so you have to extract all text from image.
        """

    def text_json_prompt():
        return """
        Understand the text extracted from Image and Give the report in Json format.
        """