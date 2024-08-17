# Guideline
## install requirements
`pip -r requirements.txt`

## cmd
`pytest -m "cache_hit" --html=reports/report.html`
-m: means using marker, 
please ref https://docs.pytest.org/en/stable/example/markers.html

## report
report would be generated after testing finished, 
`cwd/reports/report.html`
file position could be changed at cmd