from quantopian.pipeline.data.factset import Fundamentals, EquityMetadata

is_share = EquityMetadata.security_type.latest.eq('SHARE')
is_primary = EquityMetadata.is_primary.latest
primary_shares = (is_share & is_primary)
market_cap = Fundamentals.mkt_val.latest

universe = market_cap.top(1000, mask=primary_shares)