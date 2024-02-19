# Программа на Python для создания блокчейна
# Для временной метки
import datetime
# Вычисление хэша для добавления цифровой подписи к блокам
import hashlib
# Для хранения данных в блокчейне
import json
# Flask предназначен для создания веб-приложения, а jsonify - для
# отображения блокчейнаn
class Blockchain:
# Эта функция ниже создана для создания самого первого блока и установки его хэша равным "0"
    def __init__(self):
        self.current_client = ['56,housemaid,married,basic.4y,no,no,no',
                               '57,services,married,high.school,unknown,no,no',
                               '37,services,married,high.school,no,yes,no',
                               '40,admin.,married,basic.6y,no,no,no',
                               '56,services,married,high.school,no,no,yes',
                               '45,services,married,basic.9y,unknown,no,no',
                               '59,admin.,married,professional.course,no,no,no',
                               '41,blue-collar,married,unknown,unknown,no,no',
                               '24,technician,single,professional.course,no,yes,no',
                               '25,services,single,high.school,no,yes,no']

        self.chain = []
        self.create_block(proof=1, previous_hash='0')
#Добавляет нового клиента к списку клиентов
    def new_client(self):
        pass
# Эта функция ниже создана для добавления дополнительных блоков в цепочку
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'client': self.current_client[0],
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.current_client = self.current_client[1:]
        self.chain.append(block)
        return block
    @property
    def last_block(self):
        return self.chain[-1]

# Эта функция ниже создана для отображения предыдущего блока
    def print_previous_block(self):
        return self.chain[-1]
# Это функция для проверки работы и используется для успешного майнинга блока
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
        return True