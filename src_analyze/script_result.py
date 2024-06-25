import os
os.chdir('/script/script_LightningMalware/src_analyze') 

if __name__ == "__main__":
    
    with open("/script/script_LightningMalware/result/result.txt","w") as file_result:
        
        try:
            with open("/script/script_LightningMalware/result/scan_result_clam.txt", "r") as f:
                next(f)
                file_result.write(f.read())
                file_result.write("\n")
                
            with open("/script/script_LightningMalware/result/scan_result_python.txt","r") as f:
                    file_result.write("\n-------------------------- SCAN PYTHON --------------------------")
                    file_result.write(f.read())
                    file_result.write("\n")
        except Exception as e:
            file_result.write(f"Error when opening result files  {e}")