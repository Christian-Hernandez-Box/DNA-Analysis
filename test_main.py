import pytest
from main import read_dna, dna_codons, match_dna, is_criminal

def test_read_dna(tmp_path):
    dna_file = tmp_path / "test_dna.txt"
    dna_file.write_text("GTA\nGGG\nCAC\n")
    assert read_dna(dna_file) == "GTAGGGCAC"

def test_dna_codons():
    dna = "GTAGGGCAC"
    expected_codons = ['GTA', 'GGG', 'CAC']
    assert dna_codons(dna) == expected_codons

def test_match_dna():
    codons = ['GTA', 'GGG', 'CAC', 'AAA']
    assert match_dna(codons) == 3

def test_is_criminal(capsys, tmp_path):
    dna_file = tmp_path / "test_dna.txt"
    dna_file.write_text("GTAGGGCAC")
    is_criminal(dna_file)
    captured = capsys.readouterr()
    assert "# of codon matches: 3. DNA profile matches. Continue investigation." in captured.out

    dna_file.write_text("GTAGGGAAA")
    is_criminal(dna_file)
    captured = capsys.readouterr()
    assert "# of codon matches: 2. DNA profile does not match. Set Suspect free." in captured.out

if __name__ == "__main__":
    pytest.main()