<?php
/**
 * @file
 * @author REYNAUD Morgane - RENAI Yamyna - RIBEIRO Hugo
 * @version 
 */

/**
    *Function that returns the date 
    *
    *@return string the date
*/
function get_date() : string{
    $result = "";
    date_default_timezone_set('Europe/London');
    $result.= date('l jS F Y');
    return $result;
}
/**
    *Function that returns the name of the browser that the user uses
    *
    *@return string the name of the browser
*/
function get_browserw() : string {
    $user_agent = $_SERVER['HTTP_USER_AGENT'];
    $navigateur = 'Inconnu';
    if (strpos($user_agent, 'Firefox') !== false) {
        $navigateur = 'Firefox';
    } 
    elseif (strpos($user_agent, 'Chrome') !== false) {
        $navigateur = 'Chrome';
    }
    elseif (strpos($user_agent, 'Safari') !== false) {
        $navigateur = 'Safari';
    }
    elseif (strpos($user_agent, 'Edge') !== false) {
        $navigateur = 'Microsoft Edge';
    }
    elseif (strpos($user_agent, 'MSIE') !== false || strpos($user_agent, 'Trident') !== false) {
        $navigateur = 'Internet Explorer';
    }
    elseif (strpos($user_agent, 'Opera') !== false) {
        $navigateur = 'Opera';
    }
    return $navigateur;
}

/**
 * Function that reverses the css style for the page (either day.css or night.css)
 * 
 * @return string day.css or night.css
 */
function style():string{
    if(!empty($_GET["style"]) && !empty($_COOKIE["style"])){
        if($_GET["style"]=="day"){
            setcookie("style","day", time()+3600*24, '/', '', false,false);
            return "day.css";
        }
        else{
            setcookie("style","night", time()+3600*24, '/', '', false,false);
            return "night.css";
        }
    }
    else if(!empty($_COOKIE["style"])){
        if($_COOKIE["style"]=="day"){
            return "day.css";
        }
        else{
            return "night.css";
        }
    }
    else{
        setcookie("style","day", time()+3600*24, '/', '', false,false);
        return "day.css";
    }
}

/**
 * Function that reverses the style of the page
 * 
 * @return string night or day
 */
function reverseStyle():string{
    if(!empty($_GET["style"]) && !empty($_COOKIE["style"])){
        if($_GET["style"]=="day"){
            return "night";
        }
        else{
            return "day";
        }
    }
    else if(!empty($_COOKIE["style"])){
        if($_COOKIE["style"]=="day"){
            return "night";
        }
        else{
            return "day";
        }
    }
    else{
        return "night";
    }
}



/**
 * Function that returns links configured for style
 * 
 * @return string links configured
 */
function urlStyle():string{
    $res="?style=".reverseStyle();
    if(!empty($_GET["q"])){
        $val=str_replace(" ","+",$_GET["q"]);
        $res.="&amp;q=".$val;
    }    
    if(!empty($_GET["startIndex"])){
        $res.="&amp;startIndex=".$_GET["startIndex"];
    }
    return $res;
}


?>