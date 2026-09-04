import argparse, json
from .core import inspect

def main():
    p=argparse.ArgumentParser(description="Inspect an HTTP endpoint")
    p.add_argument("url")
    p.add_argument("--timeout",type=float,default=10)
    p.add_argument("--json",action="store_true")
    a=p.parse_args(); r=inspect(a.url,a.timeout)
    data={"url":r.url,"status":r.status,"elapsed":round(r.elapsed,4),"content_type":r.content_type}
    print(json.dumps(data,indent=2) if a.json else f"{r.status} {r.elapsed:.3f}s {r.content_type} {r.url}")
    return 0
