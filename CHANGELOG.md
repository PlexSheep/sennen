# Changelog

## [1.0.0](https://github.com/PlexSheep/sennen/compare/v0.3.0...v1.0.0) (2025-01-22)


### ⚠ BREAKING CHANGES

* word of the day no longer depends on the kanji
* add furigana to common and word skeleton
* **api:** do not include kanji that have no jlpt or frequency
* **api:** selection is made with better rng now #7

### Features

* **api:** generate daily entries with kanji 10 years into past and future ([0b3686d](https://github.com/PlexSheep/sennen/commit/0b3686df63fd803e59a27d5357e48b76b16da71a))
* **api:** implement the word module ([67e29d0](https://github.com/PlexSheep/sennen/commit/67e29d04efd256d7f4901f218ad283793f9fc94f))
* cli and poetry stuff ([10a2169](https://github.com/PlexSheep/sennen/commit/10a2169623f7225e094fc288642d0e38d51d8c1f))
* **cli:** add -v version flag [#27](https://github.com/PlexSheep/sennen/issues/27) ([35112e0](https://github.com/PlexSheep/sennen/commit/35112e02c3cf7a467d4b31f0b4c41b7324c72dd8))
* **cli:** clean command ([aae0e35](https://github.com/PlexSheep/sennen/commit/aae0e35d7e0e43c33683ef7e10c2ada3f5dfd73f))
* **cli:** skip-daily [#12](https://github.com/PlexSheep/sennen/issues/12) ([ca755b8](https://github.com/PlexSheep/sennen/commit/ca755b853f63d16abce7c487c5ac8914f59338bf))
* daily kanji ([dcb5fc3](https://github.com/PlexSheep/sennen/commit/dcb5fc3bea2092dc7a55d6352377413b10116ef3))
* **parse:** basic kanji parser ([39d1d1c](https://github.com/PlexSheep/sennen/commit/39d1d1ce22a617d22e01a6b46d28d73f4e324a23))
* print information in download_all_unless_exists ([9b857bc](https://github.com/PlexSheep/sennen/commit/9b857bc046a10cc66d333a24171203e3234c979b))
* **sources:** download dictionaries ([ba23f8d](https://github.com/PlexSheep/sennen/commit/ba23f8dba721c8ed7ee647c79bc691f2cd2643d5))
* **ui:** basic darkmode plus switch [#4](https://github.com/PlexSheep/sennen/issues/4) ([54fa74f](https://github.com/PlexSheep/sennen/commit/54fa74fb89175437a76d5f5bc6a266a42882ff16))
* **ui:** basic web ui ([5e0393f](https://github.com/PlexSheep/sennen/commit/5e0393f8bc0c1ec050f3e3003a338cc1d8aa1529))
* **ui:** better dark mode colors ([e8f7ee9](https://github.com/PlexSheep/sennen/commit/e8f7ee9bfd054d18b748a587350784e2a7f3fdbe))
* **ui:** better furigana ([b4914cb](https://github.com/PlexSheep/sennen/commit/b4914cb47e45cdda8bfef55f8aaac91f97f391e9))
* **ui:** better looks while loading ([8b9a228](https://github.com/PlexSheep/sennen/commit/8b9a228547d107db536d1d3433650d99d3c9f75b))
* **ui:** include the actual new sennen logo ([1bef2e5](https://github.com/PlexSheep/sennen/commit/1bef2e5d4d77a7939b5d911aab2b6fda2ee94a3e))
* **ui:** new frontend with fancy jinja templates [#9](https://github.com/PlexSheep/sennen/issues/9) ([5b5f77d](https://github.com/PlexSheep/sennen/commit/5b5f77d73b19a8d13ce2d44b89cadec421c36f5c))
* **ui:** show version in web ui ([d807d0c](https://github.com/PlexSheep/sennen/commit/d807d0ca81c263ad895621ec3cad311ba11b5ac6))
* **ui:** updated footer ([d9f29e7](https://github.com/PlexSheep/sennen/commit/d9f29e7bf5eb405afc24f4e7116e0ff19ddd694f))


### Bug Fixes

* **api:** do not include kanji that have no jlpt or frequency ([58e75e9](https://github.com/PlexSheep/sennen/commit/58e75e9ec921ffc9e6829d01acc55c44842c97e1))
* **api:** selection is made with better rng now [#7](https://github.com/PlexSheep/sennen/issues/7) ([d58ba70](https://github.com/PlexSheep/sennen/commit/d58ba70706ec3dd8c8a9b978149cfad7a7d6e18c))
* do not generate a base.html output file ([84dac0c](https://github.com/PlexSheep/sennen/commit/84dac0c2b99aa06ea801a99ac8bb3b52889aa198))
* dont use multiple cpus in test ci ([97bccc0](https://github.com/PlexSheep/sennen/commit/97bccc08a20d7f106f0dfd26681405d4dfc9d87c))
* generation handled date wrongly ([ed81eaa](https://github.com/PlexSheep/sennen/commit/ed81eaa336d1c902206dccc638c1cdf446010eb4))
* getNextDay and getPreviousDay were behaving weirdly again, so now the should theoretically REALLY REALLY work [#22](https://github.com/PlexSheep/sennen/issues/22) ([79f9902](https://github.com/PlexSheep/sennen/commit/79f9902cb87c46fee6198775953a97fd69579f53))
* linking did not work in some cases, now works for js ressource too ([ec846e8](https://github.com/PlexSheep/sennen/commit/ec846e83514a270d0d68e81e5a1de3ee92533650))
* recursive_remove failed if dir did not exist ([70787a1](https://github.com/PlexSheep/sennen/commit/70787a10d85397854662be448a79cc189c5eacda))
* remove old prints ([15e80ee](https://github.com/PlexSheep/sennen/commit/15e80ee2bc90edb6b6d7e071b16846fe123524b9))
* some of the prints did not have the (i) status symbols ([24bea92](https://github.com/PlexSheep/sennen/commit/24bea922389c2f3e08a2fc14317bd6ec28c5daa2))
* the key for the literal of the kanji was wrongfully changed ([94291f8](https://github.com/PlexSheep/sennen/commit/94291f83c1dee73415fed34fcfa1e806345d8a0b))
* **ui:** fix JS date errors ([f4851a4](https://github.com/PlexSheep/sennen/commit/f4851a4eeb17d3746e29a020e4df97f74b56a15d))
* **ui:** getNextDay and getPreviousDay now add a day by adding milliseconds [#8](https://github.com/PlexSheep/sennen/issues/8) ([ca5619b](https://github.com/PlexSheep/sennen/commit/ca5619bcedecbd42be68ea50548acb9eff356454))
* word of the day no longer depends on the kanji ([4fc0e12](https://github.com/PlexSheep/sennen/commit/4fc0e12ddc48256c6e449921dcef4cc69a7b843a))


### Documentation

* fix typo in readme link ([0b47056](https://github.com/PlexSheep/sennen/commit/0b47056368e783e65095c2184a3850072833341b))
* it said study not kanji ([553b729](https://github.com/PlexSheep/sennen/commit/553b7293b6dfa8069844401924cab1efccc354be))
* really fancy readme ([64d6cdd](https://github.com/PlexSheep/sennen/commit/64d6cddbe50283d8eafb96ee727fb31c95fbe288))
* update readme ([319f468](https://github.com/PlexSheep/sennen/commit/319f468dcfc3753ef04c190cc27914ff345e6fc7))
* update readme for new test ci and add a note for tests in the contributing section ([516390a](https://github.com/PlexSheep/sennen/commit/516390ab885f5789836d99f889f9abd36256de3d))


### Code Refactoring

* add furigana to common and word skeleton ([a49648e](https://github.com/PlexSheep/sennen/commit/a49648e81988b6835d4db84b588a202226d7418c))

## [0.3.0](https://github.com/PlexSheep/sennen/compare/v0.2.0...v0.3.0) (2025-01-20)


### Features

* **cli:** add -v version flag [#27](https://github.com/PlexSheep/sennen/issues/27) ([35112e0](https://github.com/PlexSheep/sennen/commit/35112e02c3cf7a467d4b31f0b4c41b7324c72dd8))
* print information in download_all_unless_exists ([9b857bc](https://github.com/PlexSheep/sennen/commit/9b857bc046a10cc66d333a24171203e3234c979b))


### Bug Fixes

* do not generate a base.html output file ([84dac0c](https://github.com/PlexSheep/sennen/commit/84dac0c2b99aa06ea801a99ac8bb3b52889aa198))
* dont use multiple cpus in test ci ([97bccc0](https://github.com/PlexSheep/sennen/commit/97bccc08a20d7f106f0dfd26681405d4dfc9d87c))
* generation handled date wrongly ([ed81eaa](https://github.com/PlexSheep/sennen/commit/ed81eaa336d1c902206dccc638c1cdf446010eb4))
* getNextDay and getPreviousDay were behaving weirdly again, so now the should theoretically REALLY REALLY work [#22](https://github.com/PlexSheep/sennen/issues/22) ([79f9902](https://github.com/PlexSheep/sennen/commit/79f9902cb87c46fee6198775953a97fd69579f53))


### Documentation

* fix typo in readme link ([0b47056](https://github.com/PlexSheep/sennen/commit/0b47056368e783e65095c2184a3850072833341b))
* update readme for new test ci and add a note for tests in the contributing section ([516390a](https://github.com/PlexSheep/sennen/commit/516390ab885f5789836d99f889f9abd36256de3d))

## [0.2.0](https://github.com/PlexSheep/sennen/compare/v0.1.0...v0.2.0) (2025-01-19)


### Features

* **ui:** include the actual new sennen logo ([1bef2e5](https://github.com/PlexSheep/sennen/commit/1bef2e5d4d77a7939b5d911aab2b6fda2ee94a3e))
* **ui:** show version in web ui ([d807d0c](https://github.com/PlexSheep/sennen/commit/d807d0ca81c263ad895621ec3cad311ba11b5ac6))


### Bug Fixes

* remove old prints ([15e80ee](https://github.com/PlexSheep/sennen/commit/15e80ee2bc90edb6b6d7e071b16846fe123524b9))
* some of the prints did not have the (i) status symbols ([24bea92](https://github.com/PlexSheep/sennen/commit/24bea922389c2f3e08a2fc14317bd6ec28c5daa2))


### Documentation

* really fancy readme ([64d6cdd](https://github.com/PlexSheep/sennen/commit/64d6cddbe50283d8eafb96ee727fb31c95fbe288))
* update readme ([319f468](https://github.com/PlexSheep/sennen/commit/319f468dcfc3753ef04c190cc27914ff345e6fc7))

## 0.1.0 (2025-01-19)


### ⚠ BREAKING CHANGES

* word of the day no longer depends on the kanji
* add furigana to common and word skeleton
* **api:** do not include kanji that have no jlpt or frequency
* **api:** selection is made with better rng now #7

### Features

* **api:** generate daily entries with kanji 10 years into past and future ([0b3686d](https://github.com/PlexSheep/sennen/commit/0b3686df63fd803e59a27d5357e48b76b16da71a))
* **api:** implement the word module ([67e29d0](https://github.com/PlexSheep/sennen/commit/67e29d04efd256d7f4901f218ad283793f9fc94f))
* cli and poetry stuff ([10a2169](https://github.com/PlexSheep/sennen/commit/10a2169623f7225e094fc288642d0e38d51d8c1f))
* **cli:** clean command ([aae0e35](https://github.com/PlexSheep/sennen/commit/aae0e35d7e0e43c33683ef7e10c2ada3f5dfd73f))
* **cli:** skip-daily [#12](https://github.com/PlexSheep/sennen/issues/12) ([ca755b8](https://github.com/PlexSheep/sennen/commit/ca755b853f63d16abce7c487c5ac8914f59338bf))
* daily kanji ([dcb5fc3](https://github.com/PlexSheep/sennen/commit/dcb5fc3bea2092dc7a55d6352377413b10116ef3))
* **parse:** basic kanji parser ([39d1d1c](https://github.com/PlexSheep/sennen/commit/39d1d1ce22a617d22e01a6b46d28d73f4e324a23))
* **sources:** download dictionaries ([ba23f8d](https://github.com/PlexSheep/sennen/commit/ba23f8dba721c8ed7ee647c79bc691f2cd2643d5))
* **ui:** basic darkmode plus switch [#4](https://github.com/PlexSheep/sennen/issues/4) ([54fa74f](https://github.com/PlexSheep/sennen/commit/54fa74fb89175437a76d5f5bc6a266a42882ff16))
* **ui:** basic web ui ([5e0393f](https://github.com/PlexSheep/sennen/commit/5e0393f8bc0c1ec050f3e3003a338cc1d8aa1529))
* **ui:** better dark mode colors ([e8f7ee9](https://github.com/PlexSheep/sennen/commit/e8f7ee9bfd054d18b748a587350784e2a7f3fdbe))
* **ui:** better furigana ([b4914cb](https://github.com/PlexSheep/sennen/commit/b4914cb47e45cdda8bfef55f8aaac91f97f391e9))
* **ui:** better looks while loading ([8b9a228](https://github.com/PlexSheep/sennen/commit/8b9a228547d107db536d1d3433650d99d3c9f75b))
* **ui:** new frontend with fancy jinja templates [#9](https://github.com/PlexSheep/sennen/issues/9) ([5b5f77d](https://github.com/PlexSheep/sennen/commit/5b5f77d73b19a8d13ce2d44b89cadec421c36f5c))
* **ui:** updated footer ([d9f29e7](https://github.com/PlexSheep/sennen/commit/d9f29e7bf5eb405afc24f4e7116e0ff19ddd694f))


### Bug Fixes

* **api:** do not include kanji that have no jlpt or frequency ([58e75e9](https://github.com/PlexSheep/sennen/commit/58e75e9ec921ffc9e6829d01acc55c44842c97e1))
* **api:** selection is made with better rng now [#7](https://github.com/PlexSheep/sennen/issues/7) ([d58ba70](https://github.com/PlexSheep/sennen/commit/d58ba70706ec3dd8c8a9b978149cfad7a7d6e18c))
* linking did not work in some cases, now works for js ressource too ([ec846e8](https://github.com/PlexSheep/sennen/commit/ec846e83514a270d0d68e81e5a1de3ee92533650))
* recursive_remove failed if dir did not exist ([70787a1](https://github.com/PlexSheep/sennen/commit/70787a10d85397854662be448a79cc189c5eacda))
* the key for the literal of the kanji was wrongfully changed ([94291f8](https://github.com/PlexSheep/sennen/commit/94291f83c1dee73415fed34fcfa1e806345d8a0b))
* **ui:** fix JS date errors ([f4851a4](https://github.com/PlexSheep/sennen/commit/f4851a4eeb17d3746e29a020e4df97f74b56a15d))
* **ui:** getNextDay and getPreviousDay now add a day by adding milliseconds [#8](https://github.com/PlexSheep/sennen/issues/8) ([ca5619b](https://github.com/PlexSheep/sennen/commit/ca5619bcedecbd42be68ea50548acb9eff356454))
* word of the day no longer depends on the kanji ([4fc0e12](https://github.com/PlexSheep/sennen/commit/4fc0e12ddc48256c6e449921dcef4cc69a7b843a))


### Documentation

* it said study not kanji ([553b729](https://github.com/PlexSheep/sennen/commit/553b7293b6dfa8069844401924cab1efccc354be))


### Code Refactoring

* add furigana to common and word skeleton ([a49648e](https://github.com/PlexSheep/sennen/commit/a49648e81988b6835d4db84b588a202226d7418c))
