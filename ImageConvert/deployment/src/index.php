<?php
    class WTF {
        public $var3;
        function __destruct(){
            var_dump(md5($this->var1));
            var_dump(md5($this->var2));
            if( ($this->var1 != $this->var2) && (md5($this->var1) === md5($this->var2)) ){
                echo file_get_contents(substr($this->var1,0,30).'.'); // Hint: /flag/flag
            }
        }
    }
    $sandbox = __DIR__."/sandbox/".md5($_SERVER['REMOTE_ADDR']);
    putenv("TMPDIR=".$sandbox);
    if(!file_exists($sandbox))
        mkdir($sandbox);
    if(isset($_GET['img'])){
        if(strstr($_GET['img'],"compress") === false && strstr($_GET['img'],"zip") === false && strstr($_GET['img'],"ftp") === false){
            $im = @imagecreatefrompng($_GET['img']);
            imagegd2($im);
        }else{
            die('do not support zlib & ftp,sorry :)');
        }
    }else
        highlight_file(__FILE__);
