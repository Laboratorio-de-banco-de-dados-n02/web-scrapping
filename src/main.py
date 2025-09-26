KABUM = "kabum"
TERABYTE = "terabyte"
PICHAU = "pichau"


class WebScrapping:
    def __init__(self):
        ...

    def get_better_price_of(product_name, data_source) -> int:
        
        if data_source == KABUM:
            kabum.get_better_price_of(product_name)

        elif:
            ...

        else:
            ...




# Exemplo real: quero buscar melhores precos de uma rtx
ws = WebScrapping()

values = [
    ws.get_better_price_of("RTX", KABUM)
    ws.get_better_price_of("RTX", PICHAU)
    ws.get_better_price_of("RTX", TERABYTE)
]


