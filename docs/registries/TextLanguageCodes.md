# TextLanguageCodes

- **Kind:** registry
- **Area:** [Data access](../areas/data.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The text language codes the game keeps at `g_LanguageInfo`+8, with the language pack and the name suffix each one selects.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="ja"></a>0 | `ja` | `japanese` | V | Steam language name `japanese`; resource suffix `.ja.`; pack `data/enhanced/0004.ja.pac`. |
| <a id="en"></a>1 | `en` | `english` | V | Steam language name `english`; suffix `.en.`; pack `0004.en.pac`. Also the value used when the block is absent. |
| <a id="fr"></a>2 | `fr` | `french` | V | Steam language name `french`; suffix `.fr.`; pack `0004.fr.pac`. |
| <a id="de"></a>3 | `de` | `german` | V | Steam language name `german`; suffix `.de.`; pack `0004.de.pac`. |
| <a id="cs"></a>4 | `cs` | `schinese` | V | Simplified Chinese; suffix `.cs.`; pack `0004.cs.pac`. |
| <a id="ct"></a>5 | `ct` | `tchinese` | V | Traditional Chinese; suffix `.ct.`; pack `0004.ct.pac`. |
| <a id="ko"></a>6 | `ko` | `koreana` | V | Korean; suffix `.ko.`; pack `0004.ko.pac`. |

## Behavior

- V: the current text language is the u32 at `g_LanguageInfo`+8; the table above lists the codes read in `ResourceHandle_FinishLoad` and `EventEndSlate_ShowTask`.

## Open questions

None recorded.
