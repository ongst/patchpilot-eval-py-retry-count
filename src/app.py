def run_with_retries(fn, attempts):
    for _ in range(attempts + 1):
        try:
            return fn()
        except RuntimeError:
            pass
    raise RuntimeError('failed')
