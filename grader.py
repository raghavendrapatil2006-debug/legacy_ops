# grader.py
def _safe_grade(required_phase, args, kwargs):
    """Bulletproof evaluation that will never crash the validator."""
    try:
        env = kwargs.get('env') or (args[0] if args else None)
        if env and hasattr(env, 'current_phase') and env.current_phase >= required_phase:
            return 0.99
    except Exception:
        pass
    return 0.01

def grade_phase_1(*args, **kwargs): return _safe_grade(1, args, kwargs)
def grade_phase_2(*args, **kwargs): return _safe_grade(2, args, kwargs)
def grade_phase_3(*args, **kwargs): return _safe_grade(3, args, kwargs)
def grade_phase_4(*args, **kwargs): return _safe_grade(4, args, kwargs)
def grade_phase_5(*args, **kwargs): return _safe_grade(5, args, kwargs)
def grade_phase_6(*args, **kwargs): return _safe_grade(6, args, kwargs)