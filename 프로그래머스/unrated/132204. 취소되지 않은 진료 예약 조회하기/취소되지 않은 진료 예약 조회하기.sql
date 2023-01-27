-- 코드를 입력하세요
SELECT
a.APNT_NO, 
p.PT_NAME,
a.PT_NO, # 진료과코드
a.MCDP_CD,
d.DR_NAME,
a.APNT_YMD # 진료에약일시
FROM APPOINTMENT a, DOCTOR d, PATIENT p
WHERE p.PT_NO = a.PT_NO
AND a.MDDR_ID = d.DR_ID
AND LEFT(APNT_YMD, 10) = '2022-04-13'
AND APNT_CNCL_YN = 'N'
AND APNT_CNCL_YMD IS NULL
AND a.MCDP_CD = 'CS'
ORDER BY APNT_YMD

# 2022년 4월 13일 취소되지않은
# 흉부외과(CS) 진료예약내역
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 조회
# 진료예약일시 기준 오름차순
