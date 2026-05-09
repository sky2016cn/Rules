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
        raw = line.split(",", 1)[1]
        ip.append(raw.split(",")[0])
    elif line.startswith("IP-SUFFIX,"):
        continue
    else:
        try:
            ipaddress.ip_network(line.split(",")[0], False)
            ip.append(line.split(",")[0])
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

# mihomo 域名规则集
with open(name + "_domain.list", "w", encoding="utf-8") as fout:
    for d in suffix:
        fout.write(f"+.{d}\n")
    for d in domain:
        fout.write(f"{d}\n")

# mihomo IP 规则集（供 convert-ruleset ipcidr text 使用）
with open(name + "_ip.list", "w", encoding="utf-8") as fout:
    for cidr in ip:
        fout.write(f"{cidr}\n")
