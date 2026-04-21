CREATE TABLE fighters (
    fighter_name TEXT,
    height_cm REAL,
    weight_kg REAL,
    reach_cm REAL,
    stance_clean TEXT,
    dob_clean TEXT
);

CREATE TABLE fight_results (
    event TEXT,
    bout TEXT,
    outcome TEXT,
    weightclass TEXT,
    method TEXT,
    round_clean INTEGER,
    time_seconds INTEGER,
    fighter_1 TEXT,
    fighter_2 TEXT,
    winner TEXT,
    loser TEXT
);

CREATE TABLE fight_stats (
    fighter_name TEXT,
    kd REAL,
    sub_att REAL,
    rev REAL,
    sig_strikes_landed REAL,
    sig_strikes_attempted REAL,
    total_strikes_landed REAL,
    total_strikes_attempted REAL,
    td_landed REAL,
    td_attempted REAL,
    sig_str_pct REAL,
    td_pct REAL,
    ctrl_seconds REAL
);
