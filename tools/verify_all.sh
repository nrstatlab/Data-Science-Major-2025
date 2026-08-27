#!/usr/bin/env bash
# Run every verification in this repository.
# Usage: bash tools/verify_all.sh
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
fail=0

banner() { echo; echo "=============================================="; echo "$1"; echo "=============================================="; }

banner "C labs (Course 2)"
bash "$ROOT/tools/run_c_labs.sh" || fail=$((fail+1))

banner "Python labs (Course 3)"
bash "$ROOT/tools/run_python_labs.sh" || fail=$((fail+1))

banner "Statistics labs (Course 4)"
bash "$ROOT/tools/run_stats_labs.sh" || fail=$((fail+1))

banner "SQL labs (Course 5)"
python3 "$ROOT/tools/run_sql_labs.py" || fail=$((fail+1))

banner "Syllabus extraction"
python3 "$ROOT/tools/extract_syllabus.py" "$ROOT/docs/Data-Science-Major-Sem1-2.pdf" \
    > /tmp/extract_check.md 2>/dev/null
if grep -q "no extractable text" /tmp/extract_check.md; then
    echo "FAILED: some pages produced no text"; fail=$((fail+1))
else
    echo "ok -- all $(grep -c '^## Page' /tmp/extract_check.md) pages extracted"
fi

banner "Course 6 labs (R equivalents)"
python3 "$ROOT/tools/run_r_equivalents.py" | tail -3 || fail=$((fail+1))

banner "Course 7 labs (JavaScript and DOM, under jsdom)"
if [ -d "$ROOT/tools/node_modules/jsdom" ]; then
    node "$ROOT/tools/run_web_labs.js" | tail -3 || fail=$((fail+1))
else
    echo "SKIPPED -- run: npm --prefix tools install"
fi

banner "Course 8 and 9 labs (scikit-learn, mlxtend, NumPy, Pandas)"
python3 "$ROOT/tools/run_data_labs.py" | tail -3 || fail=$((fail+1))

banner "Course 10 labs (MongoDB queries, through mongomock)"
python3 "$ROOT/tools/run_mongo_labs.py" | tail -4 || fail=$((fail+1))

banner "Course 11 labs (BI: Power Query, DAX and LOD semantics)"
python3 "$ROOT/tools/run_bi_labs.py" | tail -4 || fail=$((fail+1))

banner "Syllabus coverage"
python3 "$ROOT/tools/check_coverage.py" | tail -3 || fail=$((fail+1))

echo
if [ "$fail" -eq 0 ]; then
    echo "ALL VERIFICATIONS PASSED"
else
    echo "SUITES FAILED: $fail"
fi
[ "$fail" -eq 0 ]
