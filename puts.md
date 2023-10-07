# ⭐ Puts

## Print statement

> `puts()` has default end of line

{% code title="main.vx" overflow="wrap" %}
```cpp
//Simple hello world

fun:int main() {
    puts("Hello World!")
    return 0
}
```
{% endcode %}

### Concatenating

{% code title="main.vx" overflow="wrap" %}
```cpp
fun:int main() {
    var:string name => "Unity"
    puts("Hello " << name << "!")
    return 0
}
```
{% endcode %}
