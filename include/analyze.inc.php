<?php
/**
 * @file
 * Contient des fonctions pour analyser les fichiers.
 * Auteur : REYNAUD Morgane - RENAI Yamyna - RIBEIRO Hugo
 */

define('FILE_CLEAN_MESSAGE', "Fichier sans virus.\n");
define('FILE_INFECTED_MESSAGE', "Fichier infecté. Attention !\n");

/**
 * Analyse un fichier avec ClamAV.
 *
 * @param string $file_path Chemin du fichier à analyser.
 * @return string Message de résultat de l'analyse.
 */
function scan_with_clamav($file_path) {
    if (!class_exists('ClamAV')) {
        throw new Exception("ClamAV class not found. Please make sure clamav.php is included.");
    }

    try {
        $clamav = new ClamAV();
        $result = $clamav->scanFile($file_path);
        
        if ($result['status'] === 'OK') {
            return FILE_CLEAN_MESSAGE;
        } else {
            return FILE_INFECTED_MESSAGE;
        }
    } catch (Exception $e) {
        return "Une erreur s'est produite lors de l'analyse du fichier: " . $e->getMessage() . "\n";
    }
}
?>