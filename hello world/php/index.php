<?php

function handler($event, $context) {
    //Get function name
    $f_name = "Hello world! Function name is " . $context -> getFunctionName();
    //Print function name
    echo $f_name;
    
    return $f_name;
}