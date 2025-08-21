from __future__ import annotations

import re

COLOR_EXP = re.compile(r"#d?[mbcgyrw]<.+?>", re.DOTALL)
