from dataclasses import dataclass
from time import monotonic
from urllib.request import Request, urlopen

@dataclass(frozen=True)
class Result:
    url:str
    status:int
    elapsed:float
    content_type:str

def inspect(url:str, timeout:float=10.0)->Result:
    if timeout <= 0: raise ValueError("timeout must be positive")
    if not url.startswith(("http://","https://")): raise ValueError("URL must use HTTP or HTTPS")
    request=Request(url, method="HEAD", headers={"User-Agent":"HTTPTrace/0.1"})
    started=monotonic()
    try:
        with urlopen(request, timeout=timeout) as response:
            return Result(response.geturl(), response.status, monotonic()-started, response.headers.get_content_type())
    except Exception:
        request=Request(url, method="GET", headers={"User-Agent":"HTTPTrace/0.1"})
        with urlopen(request, timeout=timeout) as response:
            return Result(response.geturl(), response.status, monotonic()-started, response.headers.get_content_type())
