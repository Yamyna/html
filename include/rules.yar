rule Detect_Malicious {
    strings:
        $malicious_string = "malicious_pattern"

    condition:
        $malicious_string
}