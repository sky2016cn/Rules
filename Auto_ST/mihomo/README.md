# 模板说明：适用于 OpenClash、Clash Verge，不适用于 Clash for Windows
---

- 模板必须自建“🎯 全球直连”节点，才能正常使用：
   - proxies:（添加自建节点）
   -    -- {name: 🎯 全球直连, type: direct}
   - 每个策略组都自动包含“🎯 全球直连”，不需要手动再添加
   - 如果某个策略组需要默认“🎯 全球直连”，需要手动添加到最前面
   - 此模板适用于 OpenClash、Clash Verge，不适用于 Clash for Windows

---

- 1.规则集选择节点：
   - 命令说明：
   - type: select（可选择节点）
   - type: url-test（自动测速）
   - include-all: true（包含全部节点）
   - filter: "(?i)P-"  （只选择包含 P- 的节点）
   -    -- {name: 🎥 GoogleUI, type: select, include-all: true, filter: "(?i)P-"}
   - 解释：
   - include-all: true, filter: "(?i)P-"
   - 在 include-all: true（包含所有节点）中，filter: "(?i)P-"（只选择包含 P- 的节点）
     

   -    -- {name: 🎥 GoogleUI, type: select, include-all: true, exclude-type: direct}
   - 解释：
   - 在 include-all: true（包含所有节点）中，exclude-type: direct（除了🎯 全球直连）

---

- 2.选择你想要的某个节点和节点组组合：

   -    -- {name: 🎥 GoogleUI, type: select, include-all: true, filter: "(?i)P-", proxies: [🇭🇰 香港节点, 🇸🇬 新加坡节点]} 

   - 解释：在 include-all: true（包含所有节点）中，filter: "(?i)P-"（只选择包含 P- 的节点）

   - proxies: [🇭🇰 香港节点, 🇸🇬 新加坡节点] （可选择“🇭🇰 香港节点”节点组和“🇸🇬 新加坡节点”节点组）

---

- 3.选择所有的节点和节点组组合：

   -    -- {name: 🎥 GoogleUI, type: select, include-all: true, proxies: [🚀 节点选择, 🇸🇬 新加坡节点]} 

   - 解释：include-all: true（包含所有节点）
   - proxies: [🚀 节点选择, 🇸🇬 新加坡节点] （可选择“🚀 节点选择”节点组和“🇸🇬 新加坡节点”节点组）

---


创建节点组:

- 1.创建“😎 自建节点,”节点组:

   -    -- {name: 😎 自建节点, type: select, include-all: true, filter: "(?i)P-"}

   - 解释：filter: "(?i)P"    意思是只包含”P-“的节点


- 2.创建带自动测速“🇭🇰 香港节点”节点组:

   -    -- {name: 🇭🇰 香港节点, type: url-test, include-all: true, filter: "(?i)港|HK|hk|Hong Kong|HongKong|hongkong|深港", url: "https://www.gstatic.com/generate_204", interval: 300, tolerance: 50}

   - 解释：
   - type: url-test（自动测速）
   - 填入香港关键字到 filter:"" 引号中间，去匹配所有包含 香港 或 hk 等字母的节点，“url”后面是自动测速 
   - ✔注意：前面必须带参数：type: url-test，强烈建议直接使用此命令，替换名称和 filter:""引号中间的过滤名称即可


- 3.创建“🌏 全部节点,”节点组:（不建议使用，只是做个记录）

   -    -- {name: 🌏 全部节点, type: select, include-all: true}
   - 解释：
   - 包含全部节点（包含🎯 全球直连）
   - 不建议创建“🌏 全部节点”
   - 因为不能自由选择某个节点，只能选择“🌏 全部节点”节点组，没有意义


