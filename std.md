# ⚜ STD

## Split

<pre class="language-cpp" data-overflow="wrap" data-line-numbers><code class="lang-cpp"><strong>var:string greet => "Hello World"
</strong>std::vector&#x3C;std::string> hw = split(greet, " ")
outvec_str(hw)  // prints {Hello, World}</code></pre>

## Invert

{% code lineNumbers="true" %}
```cpp
var:int mynum => 32      //  32
mynum = invert(mynum)    // -32


var:int mynum => 32.40F      //  32.40
mynum = invert(mynum)    // -32.40
```
{% endcode %}

## Outvec

{% tabs %}
{% tab title="Integer" %}
{% code overflow="wrap" lineNumbers="true" %}
```cpp
std::vector<int> myVec = {1,2}
outvec_int(myVec)  //prints {1, 2}
```
{% endcode %}
{% endtab %}

{% tab title="String" %}
{% code overflow="wrap" lineNumbers="true" %}
```cpp
std::vector<std::string> myVec = {"hi","yo"}
outvec_str(myVec)  //prints {hi, yo}
```
{% endcode %}
{% endtab %}

{% tab title="Character" %}
{% code overflow="wrap" lineNumbers="true" %}
```cpp
std::vector<char> myVec = {'d','k'}
outvec_char(myVec)  //prints {d, k}
```
{% endcode %}
{% endtab %}

{% tab title="Boolean" %}
{% code overflow="wrap" lineNumbers="true" %}
```cpp
std::vector<bool> myVec = {true,false}
outvec_bool(myVec)  //prints {true, false}
```
{% endcode %}
{% endtab %}
{% endtabs %}
