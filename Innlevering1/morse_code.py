import serial


class DeCoder:
    current_message = ""
    current_letter = ""
    current_word = ""
    serial_port = None
    morse_codes = {'01': 'a', '1000': 'b', '1010': 'c', '100': 'd', '0': 'e', '0010': 'f', '110': 'g', '0000': 'h',
                   '00': 'i', '0111': 'j',
                   '101': 'k', '0100': 'l', '11': 'm', '10': 'n', '111': 'o', '0110': 'p', '1101': 'q', '010': 'r',
                   '000': 's', '1': 't',
                   '001': 'u', '0001': 'v', '011': 'w', '1001': 'x', '1011': 'y', '1100': 'z', '01111': '1',
                   '00111': '2',
                   '00011': '3',
                   '00001': '4', '00000': '5', '10000': '6', '11000': '7', '11100': '8', '11110': '9', '11111': '0'}

    def __init__(self, sport=True):
        if sport:
            self.serial_port = self.pc_connect()
        self.reset()

    def reset(self):
        # Sets all values to empty string
        self.current_message = ''
        self.current_word = ''
        self.current_letter = ''

    def pc_connect(self):
        for i in range(100):
            try:
                arduino = serial.Serial('COM' + str(i), 9600, timeout=.1)
                print("Connected to arduino")
                return arduino
            except serial.SerialException:
                pass
        exit("Arduino was not found")

    def read_one_letter(self, port=None):
        # Reads one letter/symbol (0 or 1) from the ardroino
        connection = port if port else self.serial_port
        while True:
            # Reads the input from the arduino serial connection
            return connection.read()

    def decoding_loop(self):
        # receives the signal in, and decodes it to letters, ending with a message/word to the reciver
        while True:
            s = self.read_one_letter(self.serial_port)
            for byte in s:
                self.process_signal(int(chr(byte)))

    def process_signal(self):
        # determines what the signal input is
        symbol = self.read_one_letter()
        if symbol == " ":
            self.handle_symbol_end(symbol)
        elif symbol == "N":
            self.handle_word_end()
        else:
            self.update_current_symbol()

    def update_current_symbol(self, letter):
        # adds a sign into the current letter being created
        self.current_letter += letter

    def update_current_word(self, symbol):
        # Adds a new word to current word
        self.current_word = symbol

    def handle_symbol_end(self):
        # Updates the current word and sets the letter back too " "
        self.update_current_word(self.morse_codes.get(self.symbol))
        self.current_letter = ""

    def handle_word_end(self):
        self.handle_symbol_end()
        print(self.current_word)
        self.current_word = ""
