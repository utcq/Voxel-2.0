# 📦 Packages

## Including Libraries

```cpp
@include "helloworld/helloworld.vx"
@include <helloworld/helloworld.vx>
```

## Libraries Installation

```bash
vix install helloworld std
```

## Remove Libraries

```bash
vix remove helloworld
```

## Project Management

<details>

<summary>Build Project</summary>

```cmake
vix prj build
```

</details>

<details>

<summary>Run Project</summary>

```cmake
vix prj run
```

</details>

<details>

<summary>Initialize Projct</summary>

<pre class="language-cpp"><code class="lang-cpp"><strong>vix prj init
</strong><strong>//Name: 
</strong><strong>//Version: 
</strong><strong>//Authors: 
</strong><strong>//Description: 
</strong><strong>//Dependencies: </strong></code></pre>

</details>

<details>

<summary>Setup Project</summary>

```cpp
vix prj setup
//install dependencies
```

</details>

<details>

<summary>Info Project</summary>

```cpp
vix prj info
//Name: 
//Version: 
//Authors: 
//Description: 
//Dependencies: 
```

</details>
