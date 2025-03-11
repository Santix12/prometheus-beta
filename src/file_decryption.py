import os
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, key_path, output_path=None):
    """
    Decrypt an encrypted file using a Fernet symmetric encryption key.

    Args:
        encrypted_file_path (str): Path to the encrypted file.
        key_path (str): Path to the encryption key file.
        output_path (str, optional): Path to save the decrypted file. 
                                     If None, saves in the same directory as input file.

    Returns:
        str: Path to the decrypted file.

    Raises:
        FileNotFoundError: If encrypted file or key file does not exist.
        ValueError: If key is invalid or decryption fails.
    """
    # Validate input file exists
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_path}")
    
    # Validate key file exists
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file not found: {key_path}")
    
    # Read the encryption key
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    
    # Create Fernet cipher
    try:
        cipher_suite = Fernet(key)
    except Exception as e:
        raise ValueError(f"Invalid encryption key: {str(e)}")
    
    # Read encrypted file
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    # Decrypt the file
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
    
    # Determine output path
    if output_path is None:
        # Remove .encrypted extension if present, otherwise append _decrypted
        if encrypted_file_path.endswith('.encrypted'):
            output_path = encrypted_file_path[:-10]
        else:
            output_path = encrypted_file_path + '_decrypted'
    
    # Write decrypted data
    with open(output_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    return output_path