import json
import ipaddress
import sys

file = sys.argv[1]
name = sys.argv[2]

# ================== 配置 ==================
STRICT = True          # True = 遇到未知规则就警告（推荐）
# =========================================

domain, suffix, keyword, regex, ip = [], [], [], [], []

for line in open(file, encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#") or line.startswith("//"):
        continue

    try:
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
            # 尝试作为纯 IP/CIDR 处理
            try:
                ipaddress.ip_network(line.split(",")[0], strict=False)
                ip.append(line.split(",")[0])
            except ValueError:
                if STRICT:
                    print(f"[WARN] Unknown rule type, skipped: {line}")
                    continue
                else:
                    print(f"[INFO] Treated as domain: {line}")
                    domain.append(line)

    except Exception as e:
        print(f"[ERROR] Parse failed: {line} | {e}")
        continue

# 构建 sing-box ruleset
rule = {}
if domain:   rule["domain"] = domain
if suffix:   rule["domain_suffix"] = suffix
if keyword:  rule["domain_keyword"] = keyword
if regex:    rule["domain_regex"] = regex
if ip:       rule["ip_cidr"] = ip

if not rule:
    print("Empty rule set")
    sys.exit(0)

data = {"version": 3, "rules": [rule]}
json.dump(data, open(f"{name}.json", "w", encoding="utf-8"), 
          indent=2, ensure_ascii=False)

# mihomo domain ruleset
with open(f"{name}_domain.list", "w", encoding="utf-8") as f:
    for d in suffix:
        f.write(f"+.{d}\n")
    for d in domain:
        f.write(f"{d}\n")

# mihomo ip ruleset
with open(f"{name}_ip.list", "w", encoding="utf-8") as f:
    for cidr in ip:
        f.write(f"{cidr}\n")

print(f"✓ Built: {name} | domain:{len(domain)+len(suffix)} ip:{len(ip)}")
