from src.data_fetch import fetch_data

def test_fetch_data():
    df = fetch_data("AAPL", period="5d")
    assert not df.empty