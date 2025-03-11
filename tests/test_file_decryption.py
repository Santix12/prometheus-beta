import os
import pytest
from cryptography.fernet import Fernet
import tempfile

from src.file_decryption import decrypt_file

@pytest.fixture
def setup_encrypted_file():
    """Create a temporary encrypted file for testing."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Generate a key
        key = Fernet.generate_key()
        key_path = os.path.join(tmpdir, 'test_key.key')
        with open(key_path, 'wb') as key_file:
            key_file.write(key)
        
        # Create original file
        original_text = b"This is a test file for encryption and decryption."
        original_path = os.path.join(tmpdir, 'original.txt')
        with open(original_path, 'wb') as orig_file:
            orig_file.write(original_text)
        
        # Encrypt the file
        cipher_suite = Fernet(key)
        with open(original_path, 'rb') as file_to_encrypt:
            encrypted_data = cipher_suite.encrypt(file_to_encrypt.read())
        
        encrypted_path = os.path.join(tmpdir, 'encrypted.txt.encrypted')
        with open(encrypted_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        yield {
            'key_path': key_path, 
            'encrypted_path': encrypted_path, 
            'original_text': original_text,
            'temp_dir': tmpdir
        }

def test_successful_decryption(setup_encrypted_file):
    """Test successful file decryption."""
    # Decrypt the file
    decrypted_path = decrypt_file(
        setup_encrypted_file['encrypted_path'], 
        setup_encrypted_file['key_path']
    )
    
    # Verify decryption
    with open(decrypted_path, 'rb') as decrypted_file:
        decrypted_text = decrypted_file.read()
    
    assert decrypted_text == setup_encrypted_file['original_text']

def test_nonexistent_encrypted_file():
    """Test handling of nonexistent encrypted file."""
    with pytest.raises(FileNotFoundError):
        decrypt_file('/path/to/nonexistent/file.encrypted', 'some_key.key')

def test_nonexistent_key_file(setup_encrypted_file):
    """Test handling of nonexistent key file."""
    with pytest.raises(FileNotFoundError):
        decrypt_file(
            setup_encrypted_file['encrypted_path'], 
            '/path/to/nonexistent/key.key'
        )

def test_custom_output_path(setup_encrypted_file):
    """Test decryption with a custom output path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        custom_output = os.path.join(tmpdir, 'custom_decrypted.txt')
        decrypted_path = decrypt_file(
            setup_encrypted_file['encrypted_path'], 
            setup_encrypted_file['key_path'],
            output_path=custom_output
        )
        
        assert decrypted_path == custom_output
        
        # Verify content
        with open(decrypted_path, 'rb') as decrypted_file:
            decrypted_text = decrypted_file.read()
        
        assert decrypted_text == setup_encrypted_file['original_text']