cd src
echo "Creating test set for experiment 1 - few random values"
python font_generator.py 100 100 25 25 times.ttf A 15 test_directory 
python font_generator.py 100 100 25 25 times.ttf B 25 test_directory 
python font_generator.py 100 100 25 25 times.ttf C 50 test_directory
python font_generator.py 100 100 25 25 times.ttf D 0 test_directory
python font_generator.py 100 100 25 25 times.ttf X 0 test_directory
echo "Creating test set for experiment 2 - 10%"
python font_generator.py 100 100 25 25 times.ttf A 10 test_10_directory 
python font_generator.py 100 100 25 25 times.ttf B 10 test_10_directory 
python font_generator.py 100 100 25 25 times.ttf C 10 test_10_directory
python font_generator.py 100 100 25 25 times.ttf D 10 test_10_directory
echo "Creating test set for experiment 3 - 30%"
python font_generator.py 100 100 25 25 times.ttf A 30 test_30_directory 
python font_generator.py 100 100 25 25 times.ttf B 30 test_30_directory 
python font_generator.py 100 100 25 25 times.ttf C 30 test_30_directory
python font_generator.py 100 100 25 25 times.ttf D 30 test_30_directory
echo "Creating test set for experiment 4 - 50%"
python font_generator.py 100 100 25 25 times.ttf A 50 test_50_directory 
python font_generator.py 100 100 25 25 times.ttf B 50 test_50_directory 
python font_generator.py 100 100 25 25 times.ttf C 50 test_50_directory
python font_generator.py 100 100 25 25 times.ttf D 50 test_50_directory
echo "Creating test set for experiment 5 - 90%"
python font_generator.py 100 100 25 25 times.ttf A 90 test_90_directory 
python font_generator.py 100 100 25 25 times.ttf B 90 test_90_directory 
python font_generator.py 100 100 25 25 times.ttf C 90 test_90_directory
python font_generator.py 100 100 25 25 times.ttf D 90 test_90_directory
echo "Creating test set for experiment 6 - sets of letters"
python font_generator.py 100 100 25 25 times.ttf Ai 0 test_word_directory 
python font_generator.py 100 100 25 25 times.ttf Bo 0 test_word_directory 
python font_generator.py 100 100 25 25 times.ttf Cy 0 test_word_directory
python font_generator.py 100 100 25 25 times.ttf DT 0 test_word_directory
echo "Creating test set for experiment 7 - different font"
python font_generator.py 100 100 25 25 consolas.ttf A 0 test_diff_directory 
python font_generator.py 100 100 25 25 consolas.ttf B 0 test_diff_directory 
python font_generator.py 100 100 25 25 consolas.ttf C 0 test_diff_directory