import json, ipaddress, sys

file = sys.argv[1]
name = sys.argv[2]
domain, suffix, keyword, regex, ip = [], [], [], [], []

for line in open(file, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#") or line.startswith("//"):
        continue
    if line.startswith("DOMAIN,"):
        domain.append(line.split(",", 1)[1])
    elif line.startswith("DOMAIN-SUFFIX,"):
        suffix.append(line.split(",", 1)[1])
    elif line.startswith("DOMAIN-KEYWORD,"):
        keyword.append(line.split(",", 1)[1])
    elif line.startswith("DOMAIN-REGEX,"):
        regex.append(line.split(",", 1)[1])
    elif line.startswith(("IP-CIDR,", "IP-CIDR6,")):
        ip.append(line.split(",", 1)[1])
    elif line.startswith("IP-SUFFIX,"):
        continue
    else:
        try:
            ipaddress.ip_network(line, False)
            ip.append(line)
        except:
            domain.append(line)

rule = {}
if domain:   rule["domain"]         = domain
if suffix:   rule["domain_suffix"]  = suffix
if keyword:  rule["domain_keyword"] = keyword
if regex:    rule["domain_regex"]   = regex
if ip:       rule["ip_cidr"]        = ip

if not rule:
    print("empty")
    exit(0)

data = {"version": 3, "rules": [rule]}
json.dump(data, open(name + ".json", "w"), indent=2, ensure_ascii=False)

# 同时输出 mihomo classical 格式的过滤文件
supported_prefixes = (
    "DOMAIN,", "DOMAIN-SUFFIX,", "DOMAIN-KEYWORD,", "DOMAIN-REGEX,",
    "IP-CIDR,", "IP-CIDR6,", "GEOIP,", "PROCESS-NAME,",
    "SRC-IP-CIDR,", "DST-PORT,", "SRC-PORT,",
)
with open(file, encoding="utf-8") as fin, \
     open(name + "_filtered.list", "w", encoding="utf-8") as fout:
    for line in fin:
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("//"):
            continue
        if any(s.startswith(p) for p in supported_prefixes):
            fout.write(s + "\n")
        elif "," not in s:
            # 裸域名或裸IP
            fout.write(s + "\n")
