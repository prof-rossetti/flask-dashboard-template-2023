

from pandas import DataFrame

from web_app.services.alpha import to_usd, AlphavantageService


def test_usd_formatting():
    assert to_usd(123456789.5) == '$123,456,789.50'


def test_fetch_stocks_daily():
    alpha = AlphavantageService()

    # with valid symbol, returns the data:
    df = alpha.fetch_stocks_daily(symbol="GOOGL")
    assert isinstance(df, DataFrame)
    assert not df.empty
    assert df.columns.tolist() == ['timestamp', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']
    assert len(df) >= 100

    # with invalid symbol, returns empty DataFrame:
    df = alpha.fetch_stocks_daily(symbol="OOPS")
    assert isinstance(df, DataFrame)
    assert df.empty



def test_fetch_multistock_daily():
    alpha = AlphavantageService()

    # with valid symbol, returns the data:
    result = alpha.fetch_multistock_daily(symbols=["IBM", "NFLX"])
    assert isinstance(result, dict)
    assert list(result.keys()) == ["IBM", "NFLX"]

    data = result["IBM"]
    assert isinstance(data, list)
    assert len(data) >= 100
    assert list(data[0].keys()) == ['timestamp', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']

    data = result["NFLX"]
    assert isinstance(data, list)
    assert len(data) >= 100
    assert list(data[0].keys()) == ['timestamp', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume', 'dividend_amount', 'split_coefficient']
