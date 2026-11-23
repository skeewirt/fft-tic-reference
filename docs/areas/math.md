# Math

Matrix and conversion helpers.

Functions: 7, Structures: 5, Tables: 6.

## Functions (7)

| Name | Address | Purpose |
|---|---|---|
| [Math_BuildRotationMatrix](../functions/Math_BuildRotationMatrix.md) | `0x14027471C` | Builds a 3x3 fixed-point rotation matrix (nine 16-bit values, scale 4096) from three angles using the sine and cosine tables. |
| [Math_RotateTranslateVector](../functions/Math_RotateTranslateVector.md) | `0x140274BC0` | Transforms a 3-component 16-bit vector by the current rotation matrix and translation held in globals and returns the result as three 32-bit values. |
| [Matrix2x3_Invert](../functions/Matrix2x3_Invert.md) | `0x1403D8208` | Inverts a 2x3 affine matrix (1/det with det = m0*m3 - m1*m2). |
| [Matrix2x3_Multiply](../functions/Matrix2x3_Multiply.md) | `0x1403D82F0` | Concatenates two 2x3 affine matrices (a applied first, then b); the UI's node and layer transforms use this layout [m0 m1 m2 m3 tx ty]. |
| [Matrix2x3_Rotate](../functions/Matrix2x3_Rotate.md) | `0x1403D83FC` | Rotates a 2x3 matrix by angle radians (single-precision sinf / cosf), applied AFTER m. |
| [sub_1404D66E0](../functions/sub_1404D66E0.md) | `0x1404D66E0` | Releases one reference to a shared global work block. |
| [sub_1404D6720](../functions/sub_1404D6720.md) | `0x1404D6720` | Acquires the shared global work block. |

## Structures (5)

| Name | Size (bytes) | Summary |
|---|---|---|
| [BytePopcountRow](../structs/BytePopcountRow.md) | 1 | One row of MathBytePopcount. |
| [CalendarDaysBeforeMonthRow](../structs/CalendarDaysBeforeMonthRow.md) | 2 | One row of the CalendarDaysBeforeMonth table. |
| [PrimeNumbersRow](../structs/PrimeNumbersRow.md) | 1 | One row of the PrimeNumbers table. |
| [TrigSample](../structs/TrigSample.md) | 4 | One row of the CosineTable table. |
| [WeatherBySeasonRow](../structs/WeatherBySeasonRow.md) | 56 | The whole WeatherBySeason object. |

## Tables (6)

| Name | Storage | NXD table id | Rows | Summary |
|---|---|---|---|---|
| [CalendarDaysBeforeMonth](../tables/CalendarDaysBeforeMonth.md) | Executable |  | 12 rows of 2 bytes | Days of a non-leap year before each month. |
| [CosineTable](../tables/CosineTable.md) | Executable |  | 4097 rows of 4 bytes | Shared cosine lookup: 4097 signed 32-bit samples (the last repeats the first so an interpolation can read index + 1), then 12 bytes of padding up to the sine table. |
| [MathBytePopcount](../tables/MathBytePopcount.md) | Executable |  | 256 rows of 1 byte | Number of set bits of each byte value, used to count the bits of a 32-bit mask four bytes at a time. |
| [PrimeNumbers](../tables/PrimeNumbers.md) | Executable |  | 54 rows of 1 byte | Primes below 256. |
| [SineTable](../tables/SineTable.md) | Executable |  | 4097 rows of 4 bytes | Shared sine lookup, same layout as the cosine table; 4097 samples and 8 bytes of padding up to the next object. |
| [WeatherBySeason](../tables/WeatherBySeason.md) | Executable |  | 56 bytes: 4 + 4 + 4 x 10 + 4 + 4 | Four calendar season boundaries (month and day) and, per season, ten weighted weather level adjustments. |
