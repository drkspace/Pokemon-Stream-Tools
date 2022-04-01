import scipy.stats as stats
import functools


@functools.lru_cache(maxsize=128)
def probShiny(nEncounters, odds, nShines):
    return 1 - stats.binom.cdf(k=nShines - 1, n=nEncounters, p=odds)
