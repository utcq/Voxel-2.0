---
description: How do Voxel works? Here's how
---

# ❔ How it works

## Lexer

Voxel uses Regex to split code into different tokens \
_example:_ \
&#x20;              __               <mark style="color:red;">`{'type': 'vxinclude', 'line': '"Tests/test.vx"'}`</mark>\ <mark style="color:red;">``</mark>               <mark style="color:red;"></mark><mark style="color:red;"></mark>               <mark style="color:red;"></mark><mark style="color:red;">`{'type': 'print_assignment', 'value': '"Hello!"'}`</mark>\ <mark style="color:red;">``</mark>               <mark style="color:red;"></mark><mark style="color:red;"></mark>               <mark style="color:red;"></mark><mark style="color:red;">`{'type': 'string', 'line': '"movl $10, %eax;"'}`</mark>

You can always check the Lexer output by using the argument `--debug`

