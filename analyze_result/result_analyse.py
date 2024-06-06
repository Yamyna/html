import os

def append_to_file_with_permissions(file_path, content):
    """
    Append content to a file and set the file permissions to allow read, write, and execute for all.

    :param file_path: Path to the file.
    :param content: Content to append to the file.
    """
    try:
        # Open the file in append mode and write the content
        with open(file_path, 'a') as file:
            file.write(content + '\n')

        # Change the file permissions to read, write, and execute for all
        os.chmod(file_path, 0o777)

        print(f"Content appended to {file_path} and permissions set to 777.")

    except Exception as e:
        print(f"An error occurred: {e}")


append_to_file_with_permissions('./scan_result.txt', 'Test')
