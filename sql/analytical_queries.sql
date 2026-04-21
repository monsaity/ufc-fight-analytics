SELECT COUNT(*) AS total_fighters

FROM fighters;



SELECT COUNT(*) AS total_fights

FROM fight_results;



SELECT COUNT(*) AS total_fight_stats_rows

FROM fight_stats;



SELECT method, COUNT(*) AS total

FROM fight_results

GROUP BY method

ORDER BY total DESC;



SELECT weightclass, COUNT(*) AS total

FROM fight_results

GROUP BY weightclass

ORDER BY total DESC;



SELECT winner, COUNT(*) AS wins

FROM fight_results

GROUP BY winner

ORDER BY wins DESC

LIMIT 20;



SELECT loser, COUNT(*) AS losses

FROM fight_results

GROUP BY loser

ORDER BY losses DESC

LIMIT 20;



SELECT stance_clean, COUNT(*) AS total_fighters

FROM fighters

GROUP BY stance_clean

ORDER BY total_fighters DESC;



SELECT AVG(height_cm) AS avg_height_cm,

       AVG(weight_kg) AS avg_weight_kg,

       AVG(reach_cm) AS avg_reach_cm

FROM fighters;



SELECT AVG(round_clean) AS avg_round,

       AVG(time_seconds) AS avg_time_seconds

FROM fight_results;



SELECT AVG(sig_str_pct) AS avg_sig_str_pct,

       AVG(td_pct) AS avg_td_pct,

       AVG(ctrl_seconds) AS avg_ctrl_seconds

FROM fight_stats;



SELECT fighter_name,

       AVG(sig_str_pct) AS avg_sig_str_pct

FROM fight_stats

GROUP BY fighter_name

ORDER BY avg_sig_str_pct DESC

LIMIT 20;



SELECT fighter_name,

       AVG(td_pct) AS avg_td_pct

FROM fight_stats

GROUP BY fighter_name

ORDER BY avg_td_pct DESC

LIMIT 20;



SELECT fighter_name,

       AVG(ctrl_seconds) AS avg_ctrl_seconds

FROM fight_stats

GROUP BY fighter_name

ORDER BY avg_ctrl_seconds DESC

LIMIT 20;
