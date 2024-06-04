rule Ransomware_Detection{
    meta:

        description  = "Detects ransomware activity"
        author =  "Morgane REYNAUD"
        date ="2024/06/04"
    
    strings:
        $nransom_note1 = "All your files have been encrypted" wide
        $nransom_note2 = "Your files have been encrypted" wide
        $nransom_note3 = "Your files are encrypted" wide
        $ransom_note4 = "To recover your files, you need to pay" wide
        $ransom_note5 = "Bitcoin" wide
        $ransom_note6 = "Monero" wide
        $ransom_note7 = "Ethereum" wide

        $file_marker = ".locked" ascii
        $file_marker2 = ".encrypted" ascii
        $file_marker3 = ".crypt" ascii
        $file_marker4 = ".crypted" ascii
        $file_marker5 = ".wcry" ascii
        $file_marker6 = ".wncry" ascii
        $file_marker7 = ".cryptolocker" ascii
        $file_marker8 = ".enc" ascii
        $specific_behavior = { 72 61 6E 73 6F 6D 77 61 72 65 } // hex pour 'ransomware'

    condition:
        any of them


}

rule Keylogger_Detection{
    meta:
        description  = "Detects ransomware activity"
        author =  "Morgane REYNAUD"
        date ="2024/06/04"
    strings:
        $key = "keylogger" wide
        $key2 = "key logger" wide
        $key3 = "key stroke" wide
        $key4 = "key stroke logger" wide
        $file_signature = { 4D 5A } // Signature de fichier pour les exécutables Windows
        $file_signature = { 7F 45 4C 46 } // Signature de fichier pour les exécutables Linux
        $file_signature_mac1 = { CF FA ED FE } // Signature de fichier pour les exécutables macOS (64-bit)
        $file_signature_mac2 = { CE FA ED FE } // Signature de fichier pour les exécutables macOS (32-bit)
        $specific_behavior = { 6B 65 79 6C 6F 67 67 65 72 } // hex pour 'keylogger'
        

    condition:
        any of them

}

rule Virus_Detection {
    meta:
        description  = "Detects virus activity"
        author =  "Your Name"
        date = "2024/06/04"
    
    strings:
        $virus_string1 = "This system is infected" ascii
        $virus_string2 = "Your files are locked" ascii
        $virus_string3 = "Pay to unlock your files" ascii
        $file_signature = { 50 4B 03 04 } // Signature de fichier pour un virus hypothétique
        $specific_behavior = { 76 69 72 75 73 } // hex pour 'virus'

    condition:
        any of them
}

rule Trojan_Detection {
    meta:
        description  = "Detects ransomware activity"
        author =  "Morgane REYNAUD"
        date ="2024/06/04"
    strings:
        $trojan1 = "trojan" wide
        $trojan2 = "trojan horse" wide
        $trojan3 = "trojan virus" wide
        $trojan4 = "trojan malware" wide
        $trojan5 = "trojan ransomware" wide
        $trojan6 = "trojan worm" wide
        $trojan7 = "trojan backdoor" wide
        $trojan8 = "trojan spyware" wide
        $trojan9 = "trojan dropper" wide
        $trojan10 = "trojan downloader" wide
        $trojan11 = "trojan banker" wide
        $trojan12 = "trojan rootkit" wide
        $trojan13 = "trojan adware" wide
        $trojan14 = "trojan exploit" wide
        $trojan15 = "trojan dropper" wide
        $trojan16 = "trojan exploit" wide
        $trojan17 = "trojan dropper" wide
        $trojan18 = "trojan exploit" wide
        $trojan19 = "trojan dropper" wide
        $trojan20 = "trojan exploit" wide
        $trojan21 = "trojan dropper" wide
        $trojan22 = "trojan exploit" wide
        $trojan23 = "trojan dropper" wide
        $trojan24 = "trojan exploit" wide
        $trojan25 = "trojan dropper" wide
        $trojan26 = "trojan exploit" wide
        $trojan27 = "trojan dropper" wide
        $trojan28 = "trojan exploit" wide
        $trojan29 = "trojan dropper" wide
        $trojan30 = "trojan exploit" wide
        $trojan31 = "trojan dropper" wide
        $trojan32 = "trojan exploit" wide
        $trojan33 = "trojan dropper" wide
        $trojan34 = "trojan exploit" wide
    
        $file_marker = ".trojan" ascii
        $file_marker2 = ".trojan horse" ascii
        $file_marker3 = ".trojan virus" ascii
        $file_marker4 = ".trojan malware" ascii
        $file_marker5 = ".trojan ransomware" ascii
        $file_marker6 = ".trojan worm" ascii

        $specific_behavior = { 74 72 6F 6A 61 6E } // hex pour 'trojan'
        $specific_behavior2 = { 74 72 6F 6A 61 6E 20 68 6F 72 73 65 } // hex pour 'trojan horse'
        $specific_behavior3 = { 74 72 6F 6A 61 6E 20 76 69 72 75 73 } // hex pour 'trojan virus'
        $specific_behavior4 = { 74 72 6F 6A 61 6E 20 6D 61 6C 77 61 72 65 } // hex pour 'trojan malware'
        
    condition:
        any of them
}


        