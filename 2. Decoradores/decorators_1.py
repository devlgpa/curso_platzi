
def log_transaction(func):
    def wrapper():
        print("1 Log de la transaccion...")
        func()
        print("3 Log terminado...")
    return wrapper

@log_transaction
def process_payment():
    print("2 Processando pago....")

process_payment()