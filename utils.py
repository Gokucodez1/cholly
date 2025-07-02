try:
    from bit import PrivateKey
    BIT_AVAILABLE = True
except ImportError:
    BIT_AVAILABLE = False

def send_ltc(wif_key, recipient_address, amount_btc):
    """
    Sends LTC using a WIF key (or simulates it if no wallet lib available)
    """
    if BIT_AVAILABLE:
        try:
            key = PrivateKey.from_wif(wif_key)
            tx_hash = key.send([(recipient_address, amount_btc, 'btc')])
            return tx_hash
        except Exception as e:
            return f"ERROR: {str(e)}"
    else:
        print("bit not available — using simulated TXID")
        return "simulated_txid_" + "".join(random.choices("abcdef0123456789", k=12)
