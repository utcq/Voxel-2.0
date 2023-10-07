---
description: How do Voxel works? Here's how
---

# ❔ How it works

## Lexer

Voxel uses Regex to split code into different tokens\
_example:_\
<mark style="color:red;">`{'type': 'vxinclude', 'line': '"Tests/test.vx"'}`</mark>\ <mark style="color:red;">`{'type': 'print_assignment', 'value': '"Hello!"'}`</mark>\ <mark style="color:red;">`{'type': 'string', 'line': '"movl $10, %eax;"'}`</mark>

You can always check the Lexer output by using the argument `--debug`

## Parser

Then voxel transforms the lexer output to C++ code,

<pre class="language-cpp"><code class="lang-cpp">//C++ Translation of a Simple For Loop in Voxel

#include &#x3C;string>
#include &#x3C;iostream>
#include &#x3C;vector>
#include &#x3C;fstream>
#include &#x3C;stdio.h>
#include &#x3C;std.cpp>
#include "Tests/test.cpp"

int add(int x, int y) {
    return x+y;
}
int main() {
    for(auto i: range(0, 3)) {
        std::cout &#x3C;&#x3C; "Hello!" &#x3C;&#x3C; std::endl;
    };
<strong>    return 0;
</strong>}
</code></pre>

\
You can always check the C++ code by using the argument `--save` or `--justcpp`

## Compilation

Once Voxel is converted into C++ the interpreter compiles all with `g++` \
The exact compilation command is:\
&#x20;        `g++ -w -I{dirbase}libc/ -Wall -Wextra {output + '.cpp'} -o {output}`

