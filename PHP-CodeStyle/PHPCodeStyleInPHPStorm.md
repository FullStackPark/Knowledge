

<!-- content -->

相較於其他Web後端技術，PHP的一大特色是有眾多framework支援，有macro framework如Symfony與Laravel，也有micro framework如Silex與Slim，更有較早期的CodeIgniter。

PHP的各framework蓬勃發展是一種良性競爭，但也導致各framework一直在重新製造輪子。若能讓PHP的framework各展所長，彼此互相合作，就必須大家遵守一個共同的標準，這就是`PHP-FIG`的`PSR`。

## PHP-FIG

---

為了解決這個問題，PHP各framework代表在2009年建立了PHP-FIG (**PHP Framework Interop Group**)，目的在建立各framework所遵守得共同標準，讓彼此可以互相合作。

## Framework之間互相合作

---

各framework要能互相合作使用，有3個前提必須遵守。

### Interface

各framework藉由使用相同的interface，達成互相合作。因為只要該framework實作相同的interface，別的framework就可拿來使用。

如寫log的功能，各大framework都需要，為了不讓每個framework重新製造輪子，只要有人實踐`emergency()`, `alert()`, `critical()`, `error()`, `warning()`, `notice()`, `info()`, 與`debug()`這樣interface的物件，其他framework都可以拿來用，而不用在乎它是哪個framework所提供的或如何實作。<sup>1</sup> 1事實上這就是PSR-3。

### Autoloading

各framework藉由使用相同的方法載入物件，達成互相合作。因為各framework底層載入物件的方式相同，只要同一套autoloader就能載入各framework的物件。

在此之前，各framework各自實作自己的autoloader，有的使用`\_autoload()`，有的使用`spl_autoload_register()`，導致每用一套framework，就必須去熟悉其autoloader。<sup>2</sup> 2事實上這就是PSR-4。

### Coding Style

各framework藉由使用相同的coding style，達成互相合作。因為大家使用相同的coding style，可以更容易的去trace其他framwork的code，而不用去學習新的coding style。

相同的coding style對於一個團隊也是很有幫助，假如每個成員都有自己的coding style，要去trace或了解其他成員的code將更花時間，也更難達成`code review`的目的。這也是本文希望藉由PHP-FIG的`PSR-2`來統一團隊成員中的coding style的原因。

## PSR

---

**_PSR_**是**_PHP Standard Recommendation_**的縮寫，對於各framework都會遇到的問題，PSR提出建議的解決方案，而非各framework不斷各自解決相同的問題。

目前已經正式提出的PSR如下 : 

1.  [PSR-1: Basic coding style](http://www.php-fig.org/psr/psr-1/)
2.  [PSR-2: Strict coding style](http://www.php-fig.org/psr/psr-2/)
3.  [PSR-3: Logger interface](http://www.php-fig.org/psr/psr-3/)
4.  [PSR-4: Autoloading](http://www.php-fig.org/psr/psr-4/)
5.  [PSR-7: HTTP message interface](http://www.php-fig.org/psr/psr-7/)

## PSR-2 Coding Style

---

PSR-1定義出PHP應該遵守的`最基本`coding style，PSR-2則以PSR-1為基礎定義出更嚴格的建議。以下整理出PSR-1與PSR-2所建議的coding style。

### 縮排

使用`4個space`，`不要`使用`tab`。

### 每行字數

建議在每行`80`個字左右，最多不要超過`120`個字。

### PHP標籤

* PHP必須使用`<?php ?>`或`<?= ?>`，不可以使用其他標籤。
* 若PHP不包含HTML，則不用使用結束標籤`?>`。

### 字元編碼

PHP必須使用無`BOM`的`UTF-8`編碼。<sup>3</sup> 3雖然看起來很複雜，但不用擔心，一般文字編輯器或IDE會幫你處理。

### Function

```
    function sayHello($arg1, $arg2 = 'Hi')  
    {  
        echo($arg1 . $arg2);  
    }  

    function sayHello(  
        $arg1,  
        $arg2 = 'Hi'  
    ) {  
        echo($arg1 . $arg2)  
    }  

```

* 使用`camelCase`。
* `{`必須`換行`。
* `Function名稱`與`(`之間`不要留空白`。
* 參數的`,`之`前` `不可以有空白`，而`,`之`後`需留`一個空白`。
* 參數列若提供`預設值`，則必須放在`最後一個`參數。
* 參數列允許多行寫法，第一個參數要在`新的一行`，且每一行只有`一個參數`。
* 參數列的結束`)`要在`新的一行`，且與`)`與`{`同行，之間要留`一個空白`。

### Namespace

```
    namespace Vendor\Package;  

    use FooInterface;  
    use BarClass as Bar;  
    use OtherVendor\OtherPackage\BazClass;  

    class SimpleClass   
    {  
        ...  
    }  

```

* 使用`CamelCase`命名。
* `namespace`與`<?php`之間需`空一行`。
* `namespace`宣告與`use`之間需`空一行`，`use`與`class`之間`再空一行`。
* 最上層namespace使用`公司名稱`。
* 每個class都要使用namespace，最少搭配一層namespace。

### Class

```
    class SimpleClass  
    {  
        ...  
    }  

    class ChildClass extends ParentClass  
    {  
        ...  
    }  

    class ImplClass implements ContractInterface  
    {  
        ...  
    }  

    class ImpClass implements   
        FirstInterface,  
        SecondInterface,  
        ThirdInterface  
    {  
        ...  
    }  

```

* 使用`CamelCase`命名。
* 一個class一個檔案。
* `extends`與`implements`需與class`同一行`。
* 括號`{`必須`換新的一行`。
* `implements`的interface允許多行寫法，第一個interface要在`新的一行`，且每一行只有`一個interface`。

### Interface

```
    interface PostRepositoryInterface  
    {  
        public function getLatest3Posts();  
    }  

```

* 使用`CamelCase`命名。
* 一個interface一個檔案。
* 括號`{`必須`換新的一行`。

### Trait

```
    trait LogTrait  
    {  
        public function startLog()  
        {  
            (略)  
        }  

        public function stopLog()  
        {  
            (略)  
        }  
    }  

```

* 使用`CamelCase`命名。
* 一個trait一個檔案。
* 括號`{`必須`換新的一行`。

### Constant

```
    namespace Vendor\Model;  

    class Foo  
    {  
        const VERSION = '1.0';  
        const DATE_APPROVED = '2012-06-01';  
    }  

```

* 使用`全大寫`命名。
* 單字間以`_`隔開。

### Property

```
    class SimpleClass  
    {  
        public $userName;  
        public static $userCountry;  
        private $userPassword;  
        protected $userAddr;  
    }  

```

* 使用`camelCase`命名。<sup>4</sup> 4PSR-1並沒有對property做明確規定要使用`camelCase`，只要求整個project或package風格統一即可，Laravel使用的是`camelCase`，若只有一個單字則使用小寫。
* 必須加上visibility (`public`, `protected`, `private`)。
* `static`必須加在visibility之`後`。
* `不要`再使用`var`宣告public property。
* `不要`再使用`_`宣告protected或private property。

### Method

```
    class SimpleClass  
    {  
        public function displayName()   
        {  
            ...  
        }  

        abstract protected function sendMessage()  
        {  
            ...	  
        }  


        final public function sendEmail()  
        {  
        	...  
        }  

        public static function sendSMS()  
        {  
        	...  
        }  

        final public static function sendJson()  
        {  
        	...  
        }  

        public function singleLineArgument($arg1, &$arg2, array $arg3 = [])  
        {  
            ...  
        }  

        public function multiLineArgument(  
            $arg1,  
            &$arg2,  
            array $arg3 = []  
        ) {  
           ...  
        }  
    }  

```

* 使用`camelCase`命名。
* `{`必須`換新的一行`。
* 必須加上visibility (`public`, `protected`, `private`)。
* `abstract`與`final`必須加在visibility之`前`。
* `static`必須加在visibility之`後`。
* 不要再使用`_`宣告protected或private method。
* `Method名稱`與`(`之間`不要留空白`。
* 第一個`(`之`後` `不可以有空白`，最後一個`)`之`前` `不可以有空白`。
* 參數的`,`之`前` `不可以`有`空白`，而`,`之`後`需留`一個空白`。
* 參數列若提供`預設值`，則必須放在`最後一個`參數。
* 參數列允許多行寫法，第一個參數要在`新的一行`，且每一行只有`一個參數`。
* 參數列的結束`)`要在`新的一行`，且與`)`與`{`同行，之間要留`一個空白`。

### Method and Function Calls

```
    func();  
    $foo->method1($arg1);  
    Foo::method2($arg2, $arg3);  

    $foo->method3(  
        $arg1,  
        $arg2,  
        $arg3  
    );  

```

* `Method或function名稱`與`(`之間`不可以有空白`。
* 第一個`(`之`後` `不可以有空白`，最後一個`)`之`前` `不可以有空白`。
* 每個`,`之前不可以有`空白`，每個`,`之後需留一個`空白`。
* 引數列允許多列寫法，第一個引數要在`新的一行`，且每一行只有`一個引數`。
* 參數列的結束`)`要在`新的一行`。

### Closure

```
    $closureWithArgs = function ($arg1, $arg2) {  
        // body  
    };  

    $closureWithArgsAndVars = function ($arg1, $arg2) use ($var1, $var2) {  
        // body  
    };  
   
```

* `function`與`(`之間需留`一個空白`。
* `use`前後都需要留`一個空白`。
* `{`必須與`function` `同一行`。<sup>5</sup> 5Function與method是要求`{`必須換新的一行，但closure要求`{`與`function`在同一行。
* 第一個`(`之`後` `不可以有空白`，最後一個`)`之`前` `不可以有空白`。
* 參數的`,`之前`不可以`有`空白`，而`,`之後需留一個`空白`。
* 參數列若提供`預設值`，則必須放在`最後一個`參數。

```
    $cl1 = function (  
        $arg1,  
        $arg2,  
        $arg3  
    ) {  
        ...  
    };  

    $cl2 = function () use (  
        $var1,  
        $var2,  
        $var3  
    ) {  
        ...  
    };  


    $cl3 = function (  
        $arg1,  
        $arg2,  
        $arg3  
    ) use ($var1) {  
        ...  
    };  

    $cl4 = function ($arg1) use (  
        $var1,  
        $var2,  
        $var3  
    ) {  
       ...  
    };  

    $cl5 = function (  
        $arg1,  
        $arg2,  
        $arg3  
    ) use (  
        $var1,  
        $var2,  
        $var3  
    ) {  
        ...  
    };  
  
```

* 參數列允許多行寫法，第一個參數要在`新的一行`，且每一行只有`一個參數`。
* 參數列的結束括號要在`新的一行`，且與`)`與`{`同行，之間要留`一個空白`。

### if else elseif

```
    if ($expr1) {  
        // if body  
    } elseif ($expr2) {  
        // elseif body  
    } else {  
        // else body;  
    }  
```

* `{`與`if`, `elseif`, `else`要在`同一行`，不用換行。
* `}`與`elseif`要在`同一行`，不用換行。
* `}`與`else`要在`同一行`，不用換行。

### switch case

```
    switch ($expr) {  
        case 0:  
            echo 'First case, with a break';  
            break;  
        case 1:  
            echo 'Second case, which falls through';  
            // no break  
        case 2:  
        case 3:  
        case 4:  
            echo 'Third case, return instead of break';  
            return;  
        default:  
            echo 'Default case';  
            break;  
    }  
```

* `{`與`switch`在`同一行`。
* `case`後的條件與`:`之間`不可以有空白`。
* `case`必須縮排於`switch`，而`break`必須縮排於`case`。
* PHP允許`case`內沒有`break`，但需在第一個`case`    加上`//no break`註解。

### while

```
    while ($expr) {  
        ...  
    }  
```

* `{`與`while`在`同一行`。

### do while

```
    do {  
        ...  
    } while ($expr);  
```

* `do`與`{`在`同一行`。
* `}`與`while`在`同一行`.

### for

```
    for ($i = 0; $i < 10; $i++) {  
        ...  
    }  
```

* `{`與`for`在`同一行`。
* `=`、`<`或`>`前後要留`一個空白`。
* `;`之前`不可以有空白`，之後要留`一個空白`。
* 第一個`(`之`後` `不可以有空白`，最後一個`)`之`前` `不可以有空白`。

### foreach

```
    foreach ($iterable as $key => $value) {  
        ...  
    }  
```

* `{`與`foreach`在`同一行`。
* `=>`前後要留`一個空白`。
* 第一個`(`之`後` `不可以有空白`，最後一個`)`之`前` `不可以有空白`。

### try catch

```
    try {  
        ...  
    } catch (FirstExceptionType $e) {  
        ...  
    } catch (OtherExceptionType $e) {  
        ...  
    } finally {  
        ...  
    }  
```

* `{`與`try`, `catch`要在`同一行`，不用換行。
* `}`與`catch`要在`同一行`，不用換行。
* `}`與`finally`要在`同一行`，不用換行。

## 輔助工具

---

PSR-2只是個標準，但實務上還是要搭配好用的工具來完成。

### phpcs

[PHP Code Sniffer](http://pear.php.net/package/PHP_CodeSniffer/)簡稱 **_phpcs_**，用來檢查你寫的PHP是否符合PSR-2，若完全符合則沒有任何結果，若有任何錯誤將顯示錯誤報告。這適合幫我們檢查Legacy PHP是否符合PSR-2。<sup>6</sup> 6將PHP Code Sniffer安裝到Homestead或Mac本機都可以，安裝方式都一樣，若要搭配PhpStorm就要`一定`要安裝在Mac本機。

**安裝**  

```
    $ composer global require 'squizlabs/php_codesniffer=*'  
```

```
    Changed current directory to /home/vagrant/.composer
    ./composer.json has been updated
    Loading composer repositories with package information
    Updating dependencies (including require-dev)
      - Installing squizlabs/php_codesniffer (2.3.4)
        Downloading: 100%

    Writing lock file
    Generating autoload files  
```

**測試**  

```
    $ phpcs --version  
```

```
    PHP_CodeSniffer version 2.3.4 (stable) by Squiz (http://www.squiz.net)  
```

**檢查PSR-2**  

```
    $ phpcs --standard=PSR2 Laravel/app  
```

* `Laravel`為你的專案名稱，因為我們寫的code都在app目錄下，所以直接指定PHP Code Sniffer幫我們檢查`app`目錄下所有的`.php`檔案。
* PHP Code Sniffer預設的coding style為PEAR，因為我們用的是`PSR-2`，所以要特別使用加上`--standard=PSR2`。

```
    FILE: /home/vagrant/php-cs-test/app/User.php
    ----------------------------------------------------------------------
    FOUND 3 ERRORS AFFECTING 3 LINES
    ----------------------------------------------------------------------
     13 | ERROR | [x] The first item in a multi-line implements list must
        |       |     be on the line following the implements keyword
     14 | ERROR | [x] Expected 4 spaces before interface name; 36 found
     15 | ERROR | [x] Expected 4 spaces before interface name; 36 found
    ----------------------------------------------------------------------
    PHPCBF CAN FIX THE 3 MARKED SNIFF VIOLATIONS AUTOMATICALLY
    ----------------------------------------------------------------------

    Time: 255ms; Memory: 5.25Mb  
```

* 若沒有任何違反PSR-2之處，將無任何回應，否則將出現類似如上的報表，告訴你哪個檔案有問題，錯在哪些地方。其中`FOUND`為行數。

### php-cs-fixer

[PHP Coding Standards Fixer](http://cs.sensiolabs.org/)簡稱 **_php-cs-fixer_**。雖然PHP Code Sniffer可以幫我們找出哪些code不符合PSR-2，若只有幾個檔案，我們手動改就可以，若檔案太多，就得依賴 **_php-cs-fixer_** 幫我們修正。<sup>7</sup> 7將PHP Code Standrads Fixer安裝到Homestead或Mac本機都可以，安裝方式都一樣，若要搭配PhpStorm就要`一定`要安裝在Mac本機。

**安裝**  

```
    $ composer global require fabpot/php-cs-fixer  
```

```
    Changed current directory to /home/vagrant/.composer
    Using version ^1.10 for fabpot/php-cs-fixer
    ./composer.json has been updated
    Loading composer repositories with package information
    Updating dependencies (including require-dev)
      - Installing sebastian/diff (1.3.0)
        Downloading: 100%

      - Installing symfony/stopwatch (v2.7.4)
        Downloading: 100%

      - Installing symfony/finder (v2.7.4)
        Downloading: 100%

      - Installing symfony/filesystem (v2.7.4)
        Downloading: 100%

      - Installing symfony/event-dispatcher (v2.7.4)
        Downloading: 100%

      - Installing fabpot/php-cs-fixer (v1.10)
        Downloading: 100%

    symfony/event-dispatcher suggests installing symfony/dependency-injection ()
    symfony/event-dispatcher suggests installing symfony/http-kernel ()
    Writing lock file
    Generating autoload files  
    </pre>
```

**測試**  

```
    $ php-cs-fixer  --version  
```

```
    PHP CS Fixer version 1.10 by Fabien Potencier  
```

**修正PSR-2**  

```
    $ php-cs-fixer fix Laravel/app/ --level=psr2 --verbose  
```

* `Laravel`為你的專案名稱，因為我們寫的code都在app目錄下，所以直接指定PHP-CS-Fixer幫我們檢查`app`目錄下所有的`.php`檔案。
* `--level=psr2`指定使用`PSR-2`標準來修正我們的code。
* `--verbose`表示PHP-CS-Fixer在執行時，會顯示出詳細的結果。

```
    ......F......F......
    Legend: ?-unknown, I-invalid file syntax, file ignored, .-no changes, F-fixed, E-error
       1) Http/Controllers/Controller.php (single_line_after_imports)
       2) Http/routes.php (braces)
    Fixed all files in 1.066 seconds, 6.500 MB memory used  
```

* `Lengend`表示在執行時，所執行過的動作。
* 如上圖所示，表示修正過`Controller.php`與`routes.php`。

### PhpStorm

PhpStorm對於PSR-2有以下支援 : 

1.  內建支援PSR-2。
2.  可外掛PHP Code Sniffer，讓我在寫code的同時就可提醒我們是否符合PSR-2。
3.  可外掛PHP Coding Standards Fixer，將code修正為PSR-2。

**支援PSR-2**  
**_Preferences -> Editor -> Code Style -> PHP : Set from… -> Predefined Style : PSR1/PSR2_**  
[![](http://oomusou.io/images/php/php-psr2/psr2007.png)](http://oomusou.io/images/php/php-psr2/psr2007.png)

**設定 PSR-2 所沒規定的 Code Style**  
如下圖所示，你可能會希望array的key與value能對齊，但這並不是PSR-2所規定的style，你可以自行設定。  
[![](http://oomusou.io/images/php/php-psr2/psr2009.png)](http://oomusou.io/images/php/php-psr2/psr2009.png)

**phpcs**  
**_Preferences -> Languages & Frameworks -> PHP -> Code Sniffer_**  
[![](http://oomusou.io/images/php/php-psr2/psr2000.png)](http://oomusou.io/images/php/php-psr2/psr2000.png)

指定**phpcs**路徑 : `/Users/oomusou/.composer/vendor/bin/phpcs`。<sup>8</sup> 8其中`/Users/oomusou/`為你的home directory。  
[![](http://oomusou.io/images/php/php-psr2/psr2001.png)](http://oomusou.io/images/php/php-psr2/psr2001.png)

**_Preferences -> Editor -> Inspections_**

* 將PHP Code Sniffer validation`打勾`。
* 將Coding standard選`PSR2`。

[![](http://oomusou.io/images/php/php-psr2/psr2002.png)](http://oomusou.io/images/php/php-psr2/psr2002.png)

**php-cs-fixer**  
**_Preferences -> Tools -> External Tools_**  
按`+`新增`External Tools`。  
[![](http://oomusou.io/images/php/php-psr2/psr2004.png)](http://oomusou.io/images/php/php-psr2/psr2004.png)

**Name** : `php-cs-fixer`  
**Description** : `Run php-cs on current file`  
**Program** : `/Users/oomusou/.composer/vendor/bin/php-cs-fixer`<sup>9</sup> 9其中`/Users/oomusou/`為你的home directory。  
**Parameters** : `--level=psr2 --verbose fix $FileDir$/$FileName$`  
**Working Directory** : `$ProjectFileDir$`  
[![](http://oomusou.io/images/php/php-psr2/psr2005.png)](http://oomusou.io/images/php/php-psr2/psr2005.png)

**測試**  
**測試內建的Reformat Code**

⌃ + ⌥ + L : 重新整理Coding Style。  
⌃ + ⌥ + ⇧+ L : 設定重新整理Coding Style方式。

* **Optimize imports** : 沒用到的namespace，`use`會自動移除。
* **Rearrange code** : 會自動依據Code Style的Arrangement規格將code重新排序。

[![](http://oomusou.io/images/php/php-psr2/psr2008.png)](http://oomusou.io/images/php/php-psr2/psr2008.png)

**測試PHP Code Sniffer**  
[![](http://oomusou.io/images/php/php-psr2/psr2003.png)](http://oomusou.io/images/php/php-psr2/psr2003.png)

`{`與`class`同一行，並不符合PSR-2建議，PhpStorm馬上在該行下方顯示`波浪紋`，並提示`phpcs: Openning brace of a class must be on the line after the definition`。

**測試PHP Coding Standards Fixer**  
**_Tools -> External Tools -> php-cs-fixer_**  
PHP Code Standards會幫我們的code修正成PSR-2所要求，並同時在下方顯示報告。  
[![](http://oomusou.io/images/php/php-psr2/psr2006.png)](http://oomusou.io/images/php/php-psr2/psr2006.png)

## Conclusion

---

* Function/Method與Class的`{`是否要`換行`比較爭議，不過既然PSR-2已經規定，建議遵循PSR-2。
* 經過實測結果，PHP Code Sniffer的要求會比PHP Coding Standards Fixer還嚴格，所以儘管跑過PHP Coding Standards Fixer之後，可能還需要手動修改一些地方才能通過PHP Code Sniffer。
* PhpStorm內建的coding style已經支援PSR-2，與PHP Coding Standards Fixer的差異在於 : PhpStorm允許你微調自己的coding style，甚至可以加入PSR-2沒有規定的規則，而PHP Coding Standards Fixer則完全遵循PSR-2標準。
* PhpStorm除了內建PSR-2外，還完美整合了PHP Code Sniffer與PHP Coding Standards Fixer，建議使用PhpStorm開發PHP。

