# Pollux Cipher

## Background
The Pollux Cipher is a cryptographic method that involves encoding messages in a unique way. It was developed as a variant of the Morse code where each symbol is replaced by a group of three digits. This cipher is particularly interesting because of its simplicity and its historical use in secure communications.

## Approach
Our approach to solving the Pollux Cipher involves a combination of digital signal processing and pattern recognition techniques. We use statistical analysis to decode the frequencies of the digits and map them back to their corresponding Morse code symbols.

## Installation
To install the necessary components for this project, follow these steps for your operating system:

### Windows
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pollux-cipher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pollux-cipher
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Mac
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pollux-cipher.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pollux-cipher
   ```
3. Install the required dependencies using Homebrew and pip:
   ```bash
   brew install python3
   pip3 install -r requirements.txt
   ```

## Contributing
We welcome contributions from the community. If you would like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/your_feature_name`).
3. Make your changes.
4. Submit a pull request.

## Running
To run the project, execute the following command in the terminal:

```bash
python pollux_cipher_solver.py
```

## Limitations
The current implementation of the Pollux Cipher solver has the following limitations:
- It may not accurately decode messages with non-standard or noisy Morse code sequences.
- Performance can degrade with very large datasets or messages.

For more information and updates, please check our [GitHub repository](https://github.com/yourusername/pollux-cipher).
