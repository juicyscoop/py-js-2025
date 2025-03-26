from utils import Wallet


def test_wallet_initialization():
    pln = 100
    usd = 0
    wallet = Wallet(
        initial_pln=pln,
        initial_usd=usd,
    )
    assert wallet.usd == usd
    assert wallet.pln == pln

if __name__=="__main__":
    test_wallet_initialization()


