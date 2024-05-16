cd src
echo "Network test"
python madaline_ocr.py train_directory train_directory
echo "Eksperyment 1"
python madaline_ocr.py train_directory test_directory
echo "Eksperyment 2"
python madaline_ocr.py train_directory test_10_directory
echo "Eksperyment 3"
python madaline_ocr.py train_directory test_30_directory
echo "Eksperyment 4"
python madaline_ocr.py train_directory test_50_directory
echo "Eksperyment 5"
python madaline_ocr.py train_directory test_90_directory
echo "Eksperyment 6"
python madaline_ocr.py train_directory test_word_directory
echo "Eksperyment 7"
python madaline_ocr.py train_directory test_diff_directory



