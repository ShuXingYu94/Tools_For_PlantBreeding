# Please note this programme is written with help of chatGPT!

def needleman_wunsch(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-1):
	m, n = len(seq1), len(seq2)
	score = [[0 for j in range(n + 1)] for i in range(m + 1)]
	
	# Initialize the edges with the gap penalties
	for i in range(1, m + 1):
		score[i][0] = score[i - 1][0] + gap_penalty
	for j in range(1, n + 1):
		score[0][j] = score[0][j - 1] + gap_penalty
   
	# Fill in the score matrix
	for i in range(1, m + 1):
		for j in range(1, n + 1):
			diagonal_score = score[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score)
			left_score = score[i][j - 1] + gap_penalty
			up_score = score[i - 1][j] + gap_penalty
			score[i][j] = max(diagonal_score, left_score, up_score)
   
	# Traceback and get the optimal alignment
	align1, align2 = "", ""
	i, j = m, n
	while i > 0 and j > 0:
		score_current = score[i][j]
		score_diagonal = score[i - 1][j - 1]
		score_left = score[i][j - 1]
		score_up = score[i - 1][j]
       
		if score_current == score_diagonal + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_score):
			align1 += seq1[i - 1]
			align2 += seq2[j - 1]
			i -= 1
			j -= 1
		elif score_current == score_left + gap_penalty:
			align1 += "-"
			align2 += seq2[j - 1]
			j -= 1
		elif score_current == score_up + gap_penalty:
			align1 += seq1[i - 1]
			align2 += "-"
			i -= 1
	
	# Add remaining sequence in reverse order
	while i > 0:
		align1 += seq1[i - 1]
		align2 += "-"
		i -= 1
	while j > 0:
		align1 += "-"
		align2 +=seq2[j - 1]
		j -= 1
	# Reverse sequences to get optimal alignment
	align1 = align1[::-1]
	align2 = align2[::-1]
	
	return (align1, align2)


seq1 = "AGTACGCA"
seq2 = "TATGC"
align1, align2 = needleman_wunsch(seq1, seq2)
print("Aligned sequence 1:", align1)
print("Aligned sequence 2:", align2)
